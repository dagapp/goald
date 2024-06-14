import "./table.scss";

export function Table(props) {
  const { headers, rows, size } = props;

  return (
    <div className="table__wrapper">
      <table className="table">
        <thead className="table__header">
          <tr>
            {headers?.map((header, index) => (
              <th key={index}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows?.map((row, rowIndex) => (
            <tr ley={rowIndex} className="table__row">
              {row?.map((column, colIndex) => (
                <td key={colIndex}>{column}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
