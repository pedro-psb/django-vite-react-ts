import { renderPage, useDjangoCtx } from "../components/utils/utils"

function App() {
  const { name } = useDjangoCtx()
  return <h1>Hello from About.tsx by {name}</h1>
}

renderPage(<App />)
