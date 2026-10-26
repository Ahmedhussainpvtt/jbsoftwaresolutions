import { createContext, useContext } from 'react'

const InHero = createContext(false)

export const useInHero = () => useContext(InHero)

export default function PageHero({ className = '', children }) {
  return (
    <InHero.Provider value={true}>
      <section className={`page-hero${className ? ` ${className}` : ''}`}>{children}</section>
    </InHero.Provider>
  )
}
