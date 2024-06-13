import "./table.scss";

export function Table(props) {
  const { headers, rows, size } = props;

  return (
    <div className="table__wrapper">
      <table className="table">
        <thead className="table__header">
          <tr>
            {headers?.map((header) => (
              <th>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows?.map((row) => (
            <tr className="table__row">
              {row?.map((column) => (
                <td>{column}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
