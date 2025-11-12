# AuditLab Login Prototype

## Live preview

Open [`live-preview.html`](./live-preview.html) in your browser for a one-click redirect to the hosted experience. The page automatically fetches the prebuilt data URL and launches the AuditLab login; if the redirect is blocked, a button appears so you can trigger it manually.

Prefer to launch it yourself? The underlying shareable link is stored in [`live-preview-url.txt`](./live-preview-url.txt). Copy the single-line data URL into your browser's address bar to view the AuditLab login instantly—no local server or repository checkout required.

## GitHub Pages deployment

The project now includes a `docs/` directory that mirrors the static assets so the site can be published via GitHub Pages:

1. Push the repository to GitHub (or your preferred Git provider).
2. In the repository settings, enable **Pages** and choose the `main` branch with the `/docs` folder.
3. After GitHub finishes the initial build, your site will be available at `https://<your-username>.github.io/Advanced-search-operators-list/`.
4. The deployed page will automatically load `docs/index.html`, which uses the exact same markup and styling as the local prototype.

## Local preview

To work with the AI-themed AuditLab login locally:

1. Clone or download this repository.
2. Navigate into the `frontend` directory.
3. Open `index.html` in your browser (double-clicking the file is enough), or serve the folder with any static server:
   ```bash
   # from the repository root
   cd frontend
   python3 -m http.server 5173
   ```
4. Visit `http://localhost:5173` if you started the temporary server.

Because the page is plain HTML and CSS, no build tooling or dependency installation is required.
