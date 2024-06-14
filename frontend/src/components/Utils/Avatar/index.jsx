import "./avatar.scss";

export default function Avatar(props) {
  const { image } = props;
  return (
    <div className="avatar">
      <img 
        src={image}
        alt="avatar" 
      />
    </div>
  );
}
