import { Providers } from "@app/providers";
import { AppRouter } from "@app/routers";

export default function App() {
  return (
    <Providers>
      <AppRouter />
    </Providers>
  );
}
