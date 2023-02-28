# django-vite-react-ts

This is a template to use React inside Django, in SSR time, using Vite and Typescript.

The template basically contains:

- Vite's `react-ts` template
- Django plugin [django-vite](https://github.com/MrBin99/django-vite)
- A django-tag to inject a react HMR script in development mode.

The goal is to have a smooth development environment to build apps with react and django.

## Usage

```bash
# backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirement.txt

# frontend
npm install

# development (need both servers running simultaneously)
python3 manage.py runserver
npm run dev

# production
npm run build
TODO django part
```

## Wishlist

- [x] Minimum working example
- [ ] Add TypeScript utils to integrate better with django:
    - [ ] Static tag/settings: use a TS functions to correctly load assets, links, etc in dev and prod.
    - [ ] Context Data: use a TS function to provide django context data in SSR time.
- [ ] Scaffold Multi Page Application and a REST API structure
- [ ] Add a new branch setting up Mantine UI library
- [ ] Add CI pipeline with pre-commit, gh action, etc
- [ ] Use docker?

## Resources

- [This gist](https://gist.github.com/lucianoratamero/7fc9737d24229ea9219f0987272896a2) helped me understand better how the integration should work. There is also a video link there.
- Reading [django-vite](https://github.com/MrBin99/django-vite) documenetation and the project example helped in the configuration a lot.
