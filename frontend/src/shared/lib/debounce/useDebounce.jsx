import { useState, useEffect, useRef } from "react";

export const useDebounce = (func, delay = 1200) => {
  const timer = useRef();
  const [loadingDebounce, setLoadingDebounce] = useState(false);

  useEffect(() => {
    return () => {
      if (timer.current) clearTimeout(timer.current);
    };
  }, []);

  const debouncedFunction = (...args) => {
    setLoadingDebounce(true);
    const newTimer = setTimeout(() => {
      setLoadingDebounce(false);
      func(...args);
    }, delay);
    if (timer.current) clearTimeout(timer.current);
    timer.current = newTimer;
  };

  return { debouncedFunction, loadingDebounce };
};
