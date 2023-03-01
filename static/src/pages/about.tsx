import { renderPage, useDjangoCtx, getStatic } from "../components/utils/utils"

function App() {
  const { name } = useDjangoCtx()
  return <div>
    <h1>Hello from About.tsx by {name}</h1>
    <img alt='cat' src={getStatic('pages/sample_img.jpeg')} />
  </div>
}

renderPage(<App />)
