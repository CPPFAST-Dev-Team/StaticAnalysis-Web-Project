import { createHTTPServer } from '@trpc/server/adapters/standalone';
import { appRouter } from './router';


function getAppPort(): number {
    const envPort = Number(process.env.SCANNER_SERVICE_PORT);
    if (!isNaN(envPort)) {
        return envPort;
    }
    return 4111;
}


const server = createHTTPServer({
    router: appRouter
});
const port = getAppPort();

console.info(`Launching server on port ${port}`);
server.listen(port);