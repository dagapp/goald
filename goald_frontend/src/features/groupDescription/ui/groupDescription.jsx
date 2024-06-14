import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import {
  fetchGroupDescription,
  selectGroupDescription,
  selectGroupDescriptionError,
  selectGroupDescriptionLoading,
} from "@entities/group/groupDescription";

export const GroupDescription = (props) => {
  const { id } = props;

  const groupDescription = useSelector(selectGroupDescription);
  const loading = useSelector(selectGroupDescriptionLoading);
  const error = useSelector(selectGroupDescriptionError);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchGroupDescription({ id }));
  }, []);

  const renderContent = () => {
    if (loading) {
      return "Loading...";
    }

    if (groupDescription != null) {
      return <div>{groupDescription.name}</div>;
    }
  };

  return renderContent();
};
