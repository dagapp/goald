import { BrowserRouter, Navigate, Outlet, Route, Routes } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectIsAuth } from "@entities/user/model/authSlice";

import { GroupPage } from "@pages/group";
import { LoginPage } from "@pages/login";
import { RegisterPage } from "@pages/register";
import { Layout } from "@app/layout";

const AuthRoute = (props) => {
  const { isAuth } = props;
  //return <Outlet />
  return isAuth ? <Outlet /> : <Navigate to="/login" />;
};

export function AppRouter() {
  const isAuth = useSelector(selectIsAuth);

  return (
    <BrowserRouter>
      <Routes>
        <Route element={<AuthRoute isAuth={isAuth} />}>
          <Route path="/" element={<Layout />}>
            <Route exact path="/group/:groupId" element={<GroupPage />} />
          </Route>
        </Route>

        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </BrowserRouter>
  );
}
