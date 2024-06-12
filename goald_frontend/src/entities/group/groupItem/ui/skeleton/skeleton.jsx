import Skeleton, { SkeletonTheme } from "react-loading-skeleton";

import "react-loading-skeleton/dist/skeleton.css";
import "./skeleton.scss";

export function GroupItemSkeleton() {
  return (
    <SkeletonTheme
      baseColor="var(--ui-color-secondary)"
      highlightColor="var(--ui-color-action)"
    >
      <div className="group-item-skeleton">
        <div className="group-item-skeleton__avatar">
          <Skeleton
            borderRadius={"var(--ui-size-border_radius-small)"}
            width={"var(--ui-size-icon-large)"}
            height={"var(--ui-size-icon-large)"}
          />
        </div>
        <div className="group-item-skeleton__overview">
          <div className="group-item-skeleton__overview_field">
            <Skeleton />
          </div>
          <div className="group-item-skeleton__overview_field">
            <Skeleton />
          </div>
        </div>
      </div>
    </SkeletonTheme>
  );
}
