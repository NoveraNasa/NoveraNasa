# Installation

This folder is ready for the special GitHub profile repository:

`https://github.com/NoveraNasa/NoveraNasa`

## Upload through the GitHub website

1. Open the repository `NoveraNasa/NoveraNasa`.
2. Choose **Add file → Upload files**.
3. Upload every file and folder from this package.
4. Commit the files to the `main` branch.
5. Open **Actions → Update profile card → Run workflow**.
6. Return to `https://github.com/NoveraNasa`.

The workflow uses GitHub's built-in `GITHUB_TOKEN`; no personal access token is required.

## Important

Keep these exact paths:

- `.github/workflows/update-profile.yml`
- `README.md`
- `update_profile.py`
- `dark_mode.template.svg`
- `light_mode.template.svg`

The workflow generates:

- `dark_mode.svg`
- `light_mode.svg`

## Local test

Run:

```bash
python update_profile.py
```

Then open `dark_mode.svg` or `light_mode.svg` in a browser.
