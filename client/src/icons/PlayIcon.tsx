export interface PlayIconProps {
  className?: string;
}

export const PlayIcon = ({ className }: PlayIconProps) => (
  <svg
    xmlns='http://www.w3.org/2000/svg'
    className={className}
    viewBox='0 0 20 20'
    fill='currentColor'
  >
    <path d='M4.5 3.5l11 6.5-11 6.5v-13z' />
  </svg>
);
