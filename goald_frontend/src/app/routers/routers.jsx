import { BrowserRouter, Route, Routes } from "react-router-dom";

import { GroupPage } from "@pages/group";
import { LoginPage } from "@pages/login";
import { RegisterPage } from "@pages/register";
import { Layout } from "@app/layout";

export function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route exact path="/group/:groupId" element={<GroupPage />} />
        </Route>

        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </BrowserRouter>
  );
}
