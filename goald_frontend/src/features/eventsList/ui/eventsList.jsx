import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import Skeleton, { SkeletonTheme } from "react-loading-skeleton";
import "react-loading-skeleton/dist/skeleton.css";

import { Table } from "@shared/ui/table";

import {
  fetchEvents,
  selectGroupEvents,
  selectEventsError,
  selectEventsLoading,
} from "@features/eventsList";

import "./eventsList.scss";

export const EventsList = (props) => {
  const { id } = props;

  const events = useSelector(selectGroupEvents);
  const error = useSelector(selectEventsError);
  const loading = useSelector(selectEventsLoading);

  const dispatch = useDispatch();

  const tableSkeletonRow = [
    <Skeleton width={"100px"} />,
    <Skeleton width={"100px"} />,
    <Skeleton width={"100px"} />,
  ];

  useEffect(() => {
    dispatch(fetchEvents({ id }));
  }, []);

  const renderContent = () => {
    if (loading) {
      return (
        <div className="events-list__loading">
          <SkeletonTheme
            baseColor="var(--ui-color-secondary)"
            highlightColor="var(--ui-color-action)"
          >
            <Table
              headers={tableSkeletonRow}
              rows={[tableSkeletonRow, tableSkeletonRow, tableSkeletonRow]}
            />
          </SkeletonTheme>
        </div>
      );
    }

    if (error) {
      return <span className="events-list__error">{error.messageError}</span>;
    }

    if (events != null && events.length > 0) {
      return (
        <div className="events-list__results">
          <Table
            headers={["Timestamp", "Message", "Event Type"]}
            rows={events?.map((event) => [
              event.timestamp,
              event.text,
              event.type,
            ])}
          />
        </div>
      );
    }
  };

  return <div className="events-list">{renderContent()}</div>;
};