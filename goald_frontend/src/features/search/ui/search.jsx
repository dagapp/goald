import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import clsx from "clsx";

import {
  fetchSearch,
  selectSearchGroups,
  selectSearchError,
  selectSearchLoading,
} from "@features/search";

import { Group } from "@entities/group";
import { GroupSkeleton } from "@entities/group";

import { useDebounce } from "@shared/lib/debounce";
import { Dropdown } from "@shared/ui/dropdown";
import { Input } from "@shared/ui/input";

import "./search.scss";

export const Search = (props) => {
  const { className } = props;

  const [isOpen, setIsOpen] = useState(false);
  const [valueSearch, setValueSearch] = useState("");

  const groups = useSelector(selectSearchGroups);
  const loading = useSelector(selectSearchLoading);
  const error = useSelector(selectSearchError);
  const dispatch = useDispatch();

  const { debouncedFunction: getResultSearchDebounce, loadingDebounce } =
    useDebounce((searchString) => dispatch(fetchSearch({ searchString })));

  const onChangeSearch = (event) => {
    setValueSearch(event.target.value);
    getResultSearchDebounce(event.target.value);
  };

  const renderContent = () => {
    if (loading || loadingDebounce) {
      return (
        <div className="search__loading">
          <GroupSkeleton />
          <GroupSkeleton />
          <GroupSkeleton />
        </div>
      );
    }

    if (error) {
      return <span className="search__error">{error.messageError}</span>;
    }

    // Change? groups <-> groups != null
    if (groups != null && groups.length > 0) {
      return (
        <div className="search__results">
          {groups?.map((item, index) => (
            <Group
              key={item.name} // Should Be replaced with Group ID
              avatar={item.avatar}
              name={item.name}
              tag={item.tag}
              url={item.url} // Should Be replaced with Group URL
            />
          ))}
        </div>
      );
    }
  };

  return (
    <div className={clsx("search", className)}>
      <Dropdown
        isOpen={isOpen}
        labelElement={
          <Input
            placeholder="Search Groups"
            value={valueSearch}
            onChange={onChangeSearch}
            onBlur={() => setIsOpen(false)}
            onFocus={() => setIsOpen(true)}
            className={"search__input"}
          />
        }
        content={renderContent()}
        className="search__dropdown"
      />
    </div>
  );
};
