type Log = {
    logId: number;
    message: string;
};

class LogAggregator {
    private serviceLogs: { [key: number]: Log[] };
    private machineLogs: { [key: number]: Log[] };
    private machines;
    private services;

    constructor(machines: number, services: number) {
        console.log('here');

        this.machines = machines;
        this.services = services;
        this.serviceLogs = {};
        this.machineLogs = {};
    }

    pushLog(
        logId: number,
        machineId: number,
        serviceId: number,
        message: string
    ): void {
        // check if already exists
        if (machineId in this.machineLogs) {
            this.machineLogs[machineId].push({ logId, message });
        } else {
            this.machineLogs[machineId] = [{ logId, message }];
        }

        if (serviceId in this.serviceLogs) {
            this.serviceLogs[serviceId].push({ logId, message });
        } else {
            this.serviceLogs[serviceId] = [{ logId, message }];
        }
    }

    getLogsFromMachine(machineId: number): number[] {
        // return this.machineLogs.map((idx, log) => log[idx] log[.logId)
        // console.log(this.machineLogs)
        if (!(machineId in this.machineLogs)) {
            return [];
        }

        return this.machineLogs[machineId].map((log) => log.logId);
    }

    getLogsOfService(serviceId: number): number[] {
        if (!(serviceId in this.serviceLogs)) {
            return [];
        }

        return this.serviceLogs[serviceId].map((log) => log.logId);
    }

    search(serviceId: number, searchString: string): string[] {
        const logs = this.serviceLogs[serviceId];
        if(!logs) return [];
        const result: string[] = [];
        for (let i = 0; i < logs.length; i++) {
            if (logs[i].message.indexOf(searchString) != -1) {
                result.push(logs[i].message);
            }
        }
        return result;
    }
}