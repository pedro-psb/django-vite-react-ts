import React from 'react'
import ReactDOM from 'react-dom/client'
import AppShell from '../AppShell'

/**
* # Shortcut function to render the App  in the dom
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
