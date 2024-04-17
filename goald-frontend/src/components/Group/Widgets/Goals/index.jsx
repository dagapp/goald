import Progressbar from "@components/Utils/Progressbar";
import Card from "@components/Utils/Card";
import "./Goals.scss";

export default function Goals(props) {
  const {
    goals
  } = props
  return (
    <Card
      title={"Goals"}
      children={
        <div className="goals-cards">
          {goals.map((goal, index) => {
            return (
              <div key={index} className="goals-card">
                <h3>{goal.title}</h3>
                <Progressbar
                  daysLeft={goal.daysLeft}
                  amount={goal.amount}
                  goal={goal.goal}
                  percentage={goal.percentage}
                />
              </div>
            );
          })}
        </div>
      }
    />
  );
}
