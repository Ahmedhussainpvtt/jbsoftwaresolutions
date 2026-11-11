export default function CalendarIcon({ size = 18 }) {
  return (
    <svg className="call-ico" viewBox="0 0 24 24" width={size} height={size} aria-hidden="true">
      <rect x="3.5" y="5" width="17" height="15.5" rx="3" fill="none" stroke="currentColor" strokeWidth="2" />
      <path d="M3.5 10h17M8 3v4M16 3v4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
    </svg>
  )
}
