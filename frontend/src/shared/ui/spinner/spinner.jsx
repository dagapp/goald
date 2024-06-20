import clsx from "clsx";
import "./spinner.scss";

export function Spinner(props) {
  const { color, size } = props;
  return (
    <span
      className={clsx(
        "spinner",
        "spinner_color_" + color,
        "spinner_size_" + size
      )}
    />
  );
}
