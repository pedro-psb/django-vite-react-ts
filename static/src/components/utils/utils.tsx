import React from 'react'
import ReactDOM from 'react-dom/client'
import AppShell from '../AppShell'

/**
* Shortcut function to render the App  in the dom
*
* Use it to render page components that will be imported in a django-html file
* @param {boolean?} defaultAppShell - whether to use the default AppShell wrapper component
*/
export function renderPage(component: JSX.Element, defaultAppShell: boolean = true) {
  ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
    <React.StrictMode>
      {defaultAppShell ?
        <AppShell>
          {component}
        </AppShell>
        : component
      }
    </React.StrictMode>
  )
}

/**
* Return context passed by a view
*
* The django _base.html template transform the context data passed as `context={'context': ...}`
* to a serliazed json inside  `<script id='context-data'> ... </script>`
*
* To do the same with other context data (not directly passed as context) you may try to
* do the process. Adam Johson wrote a greate blog post about it:
* - [read more](https://adamj.eu/tech/2022/10/06/how-to-safely-pass-data-to-javascript-in-a-django-template/)
*/
export function useDjangoCtx() {
  const context_script_element: HTMLElement = document.getElementById('context-data')!
  const context = JSON.parse(context_script_element.textContent || "");
  return context
}

/**
* Get the static url as provided by {% static %}
*
* WARNING: currently it is just a workaround to dev mode.
* This does not work in production
*
* TODO
* - devmode improvement: use django-vite settings to build this path dynamically
* - prod: make it work 
*/
export function getStatic(filename: string) {
  return `http://localhost:3000/static/${filename}`
}
