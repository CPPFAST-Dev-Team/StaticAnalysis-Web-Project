import { createHTTPServer } from '@trpc/server/adapters/standalone';
import { appRouter } from './router';


const server = createHTTPServer({
    router: appRouter
});
const port = 6000;

console.info(`Launching server on port ${port}`);
server.listen(port);