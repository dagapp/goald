import "./Card.scss";

export default function Card(props) {
  const {
    title,
    children,
  } = props
  return (
    <div className="card">
      {title && <h2 className="card__title">{title}</h2>}
      <div>{children}</div>
    </div>
  );
}