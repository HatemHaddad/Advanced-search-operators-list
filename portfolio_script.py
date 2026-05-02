#!/usr/bin/env python3

import math
import numpy as np
import pandas as pd
import yfinance as yf
from tabulate import tabulate

def main():
    tickers = ["CVX", "IBM"]
    start_date = "2018-01-01"
    end_date = "2026-05-02"
    trading_days = 252

    raw = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False
    )

    if isinstance(raw.columns, pd.MultiIndex):
        stock_prices = raw["Close"].copy()
    else:
        stock_prices = raw[["Close"]].copy()
        stock_prices.columns = tickers

    stock_prices.dropna(inplace=True)

    if len(stock_prices) < 2:
        raise ValueError("Not enough price rows after cleaning to compute returns.")

    print("\nDownloaded prices (head):")
    print(stock_prices.head())
    print("\nDownloaded prices (tail):")
    print(stock_prices.tail())

    annual_returns = (
        (stock_prices.iloc[-1] / stock_prices.iloc[0]) ** (trading_days / len(stock_prices)) - 1
    )

    price_returns = stock_prices.pct_change().dropna()
    annual_std_dev = price_returns.std(ddof=0) * math.sqrt(trading_days)

    cvx_ticker, ibm_ticker = "CVX", "IBM"

    a = (1 / annual_std_dev[cvx_ticker]) / (
        (1 / annual_std_dev[cvx_ticker]) + (1 / annual_std_dev[ibm_ticker])
    )
    b = (1 / annual_std_dev[ibm_ticker]) / (
        (1 / annual_std_dev[cvx_ticker]) + (1 / annual_std_dev[ibm_ticker])
    )

    print("\nVolatility and capital allocation:")
    print(tabulate(
        [
            [cvx_ticker, annual_std_dev[cvx_ticker], a],
            [ibm_ticker, annual_std_dev[ibm_ticker], b]
        ],
        headers=["Stock", "Annualized Std Dev", "Capital Allocation"],
        floatfmt=(".0f", ".6f", ".6f")
    ))

    portfolio_returns = a * annual_returns[cvx_ticker] + b * annual_returns[ibm_ticker]
    print(f"\nPortfolio annualized return: {portfolio_returns * 100:.2f}%")

    cov_cvx_ibm = np.cov(
        price_returns[cvx_ticker],
        price_returns[ibm_ticker],
        bias=True
    ) * trading_days

    portfolio_std_dev = math.sqrt(
        (a ** 2) * (annual_std_dev[cvx_ticker] ** 2)
        + (b ** 2) * (annual_std_dev[ibm_ticker] ** 2)
        + 2 * a * b * cov_cvx_ibm[0, 1]
    )
    print(f"Portfolio annualized standard deviation: {portfolio_std_dev * 100:.2f}%")

    ratio = portfolio_returns / portfolio_std_dev if portfolio_std_dev != 0 else np.nan
    print(f"Portfolio return / portfolio std dev: {ratio:.2f}")

if __name__ == "__main__":
    main()
