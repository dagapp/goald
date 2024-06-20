import "./progressBar.scss";

export function ProgressBar(props) {
  const { percentage } = props;

  return (
    <div className="progress-bar">
      <span
        className="progress-bar__filler"
        style={{ width: `${percentage}%` }}
      ></span>
    </div>
  );
}
