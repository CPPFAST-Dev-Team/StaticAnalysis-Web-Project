import AdmZip from "adm-zip";
import { basename, join } from "node:path";
import { StorageAdapter } from "./adapter";
import { extractFilesTo, getFileSharingLocation } from "../utils/file-system";


/**
 * Storage interface for working with locally available zip files.
 */
export class LocalZipStorage extends StorageAdapter {
    protected async downloadFiles(id: string, directory: string): Promise<void> {
        const fileName = basename(id);
        const fullPath = join(getFileSharingLocation(), fileName);
        const archive = new AdmZip(fullPath);
        await extractFilesTo(archive, directory);
    }
}