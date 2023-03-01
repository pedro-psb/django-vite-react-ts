import "../assets/global.css"
import "../assets/normalize.css"

export default function AppShell({ children }: { children: any }) {
  return (
    <>
      <header>
        <div>
          <a href="/">Home</a>{" | "}
          <a href="/about">About</a>
        </div>
      </header>
      <main>{children}</main>
      <footer>This is the footer section</footer>
    </>
  )
}
