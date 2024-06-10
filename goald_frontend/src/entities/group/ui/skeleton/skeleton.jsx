import Skeleton, { SkeletonTheme } from "react-loading-skeleton";

import "react-loading-skeleton/dist/skeleton.css";
import "./skeleton.scss";

export function GroupSkeleton() {
  return (
    <SkeletonTheme
      baseColor="var(--ui-color-secondary)"
      highlightColor="var(--ui-color-action)"
    >
      <div className="group-skeleton">
        <div className="group-skeleton__avatar">
          <Skeleton
            borderRadius={"var(--ui-size-border_radius-small)"}
            width={"var(--ui-size-icon-large)"}
            height={"var(--ui-size-icon-large)"}
          />
        </div>
        <div className="group-skeleton__overview">
          <div className="group-skeleton__overview_field">
            <Skeleton />
          </div>
          <div className="group-skeleton__overview_field">
            <Skeleton />
          </div>
        </div>
      </div>
    </SkeletonTheme>
  );
}
