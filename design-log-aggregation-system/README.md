<h2>  Design Log Aggregation System</h2><hr><div><p>Implement a <strong>Log Aggregation System</strong> which aggregates logs from various services in a datacenter and provides search APIs.</p>

<p>Design the <code>LogAggregator</code> class:</p>

<ul>
	<li><code>LogAggregator(int machines, int services)</code> Initializes the object with <code>machines</code> and <code>services</code> representing the number of machines and services in the datacenter, respectively.</li>
	<li><code>void pushLog(int logId, int machineId, int serviceId, String message)</code> Adds a log with id <code>logId</code> notifying that the machine <code>machineId</code> sent a string <code>message</code> while executing the service <code>serviceId</code>.</li>
	<li><code>List&lt;Integer&gt; getLogsFromMachine(int machineId)</code> Returns a list of ids of all logs added by machine <code>machineId</code>.</li>
	<li><code>List&lt;Integer&gt; getLogsOfService(int serviceId)</code> Returns a list of ids of all logs added while running service <code>serviceId</code> on any machine.</li>
	<li><code>List&lt;String&gt; search(int serviceId, String searchString)</code> Returns a list of messages of all logs added while running service <code>serviceId</code> where the message of the log contains <code>searchString</code> as a substring.</li>
</ul>

<p><strong>Note</strong> that:</p>

<ul>
	<li>The entries in each list should be in the order they were added, i.e., the older logs should precede the newer logs.</li>
	<li>A machine can run multiple services more than once. Similarly, a service can be run on multiple machines.</li>
	<li>All <code>logId</code> may <strong>not</strong> be ordered.</li>
	<li>A <strong>substring</strong> is a contiguous sequence of characters within a string.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["LogAggregator", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "getLogsFromMachine", "getLogsOfService", "search", "search"]
[[3, 3], [2322, 1, 1, "Machine 1 Service 1 Log 1"], [2312, 1, 1, "Machine 1 Service 1 Log 2"], [2352, 1, 1, "Machine 1 Service 1 Log 3"], [2298, 1, 1, "Machine 1 Service 1 Log 4"], [23221, 1, 2, "Machine 1 Service 2 Log 1"], [23121, 1, 2, "Machine 1 Service 2 Log 2"], [23222, 2, 2, "Machine 2 Service 2 Log 1"], [23122, 2, 2, "Machine 2 Service 2 Log 2"], [23521, 1, 2, "Machine 1 Service 2 Log 3"], [22981, 1, 2, "Machine 1 Service 2 Log 4"], [23522, 2, 2, "Machine 2 Service 2 Log 3"], [22982, 2, 2, "Machine 2 Service 2 Log 4"], [2], [2], [1, "Log 1"], [2, "Log 3"]]
<strong>Output</strong>
[null, null, null, null, null, null, null, null, null, null, null, null, null, [23222, 23122, 23522, 22982], [23221, 23121, 23222, 23122, 23521, 22981, 23522, 22982], ["Machine 1 Service 1 Log 1"], ["Machine 1 Service 2 Log 3", "Machine 2 Service 2 Log 3"]]

<strong>Explanation</strong>
LogAggregator logAggregator = new LogAggregator(3, 3); // There are 3 machines and 3 services
logAggregator.pushLog(2322, 1, 1, "Machine 1 Service 1 Log 1");
logAggregator.pushLog(2312, 1, 1, "Machine 1 Service 1 Log 2");
logAggregator.pushLog(2352, 1, 1, "Machine 1 Service 1 Log 3");
logAggregator.pushLog(2298, 1, 1, "Machine 1 Service 1 Log 4");
logAggregator.pushLog(23221, 1, 2, "Machine 1 Service 2 Log 1");
logAggregator.pushLog(23121, 1, 2, "Machine 1 Service 2 Log 2");
logAggregator.pushLog(23222, 2, 2, "Machine 2 Service 2 Log 1");
logAggregator.pushLog(23122, 2, 2, "Machine 2 Service 2 Log 2");
logAggregator.pushLog(23521, 1, 2, "Machine 1 Service 2 Log 3");
logAggregator.pushLog(22981, 1, 2, "Machine 1 Service 2 Log 4");
logAggregator.pushLog(23522, 2, 2, "Machine 2 Service 2 Log 3");
logAggregator.pushLog(22982, 2, 2, "Machine 2 Service 2 Log 4");
logAggregator.getLogsFromMachine(2); // return [23222, 23122, 23522, 22982]
                                     // Machine 2 added 4 logs, so we return them in the order
                                     // they were added.
logAggregator.getLogsOfService(2); // return [23221, 23121, 23222, 23122, 23521, 22981, 23522, 22982]
                                   // 8 logs were added while running service 2 on a machine.
logAggregator.search(1, "Log 1"); // return ["Machine 1 Service 1 Log 1"]
                                  // There is only one log that was added while running service 1
                                  // and contains "Log 1".
logAggregator.search(2, "Log 3"); // return ["Machine 1 Service 2 Log 3", "Machine 2 Service 2 Log 3"]
                                  // 2 logs were added while running service 2 that contain "Log 3".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= machines, services &lt;= 20</code></li>
	<li><code>1 &lt;= logId &lt;= 10<sup>5</sup></code></li>
	<li>All <code>logId</code> are <strong>unique</strong>.</li>
	<li><code>0 &lt;= machineId &lt;= machines - 1</code></li>
	<li><code>0 &lt;= serviceId &lt;= services - 1</code></li>
	<li><code>1 &lt;= message.length, searchString.length &lt;= 500</code></li>
	<li><code>message</code> and <code>searchString</code> consist of letters, digits, and <code>' '</code> only.</li>
	<li>At most <code>100</code> calls <strong>in total</strong> will be made.</li>
	<li>At least <strong>one</strong> call <strong>in total</strong> will be made to <code>getLogsFromMachine</code>, <code>getLogsOfService</code>, and <code>search</code>.</li>
</ul>
</div>