import { useState } from "react";
import clsx from "clsx";

import "./input.scss";

export function Input(props) {
  const {
    value,
    onChange,
    onBlur,
    onFocus,
    onKeyDown,
    placeholder,
    className,
  } = props;

  const [inputData, setinputData] = useState("");
  const onChangeinputData = (event) => {
    setinputData(event.target.value);
  };

  return (
    <input
      className={clsx("input", className)}
      type="text"
      value={value ?? inputData}
      placeholder={placeholder}
      onBlur={onBlur}
      onFocus={onFocus}
      onChange={onChange ?? onChangeinputData}
      onKeyDown={onKeyDown}
    />
  );
}
