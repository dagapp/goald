import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import {
  fetchGroupList,
  selectGroupList,
  selectGroupListLoading,
  selectGroupListError,
} from "@features/groupList";

import { GroupItem } from "@entities/group/groupItem";
import { GroupItemSkeleton } from "@entities/group/groupItem";

import "./groupList.scss";

export const GroupList = (props) => {
  const groups = useSelector(selectGroupList);
  const loading = useSelector(selectGroupListLoading);
  const error = useSelector(selectGroupListError);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchGroupList());
  }, []);

  const renderContent = () => {
    if (loading) {
      return (
        <div className="group-list__loading">
          <GroupItemSkeleton />
          <GroupItemSkeleton />
          <GroupItemSkeleton />
          <GroupItemSkeleton />
          <GroupItemSkeleton />
        </div>
      );
    }

    if (error) {
      return <span className="group-list__error">{error.messageError}</span>;
    }

    // On the final stage
    if (groups != null && groups.length > 0) {
      return (
        <div className="group-list__results">
          {groups?.map((group) => (
            <GroupItem
              key={group.id}
              id={group.id}
              avatar={group.avatar}
              name={group.name}
              tag={group.tag}
            />
          ))}
        </div>
      );
    }
  };

  return <div className="group-list">{renderContent()}</div>;
};
