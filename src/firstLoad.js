// True while rendering on the server and during the first client hydration.
// Server HTML must paint visible content, so entrance animations that start
// hidden are skipped until the app has mounted once.
let first = true

export const isFirstLoad = () => first

export function markLoaded() {
  first = false
}
