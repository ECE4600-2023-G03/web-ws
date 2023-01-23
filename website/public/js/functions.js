// When we receive a message on /my_topic, add its data as a list item to the "messages" ul
function start_collection() {
    // Create a listener for /my_topic
    const status_topic = new ROSLIB.Topic({
        ros,
        name: "/status_topic",
        messageType: "std_msgs/String",
    });

    var str = new ROSLIB.Message({
        data: 'Collecting'
    });

    status_topic.publish(str);

    status_topic.subscribe((message) => {
        document.getElementById("messages").innerHTML = message.data;
    });

    // Create a listener for /twist_topic
    const bool_topic = new ROSLIB.Topic({
        ros,
        name: "/bool_topic",
        messageType: "std_msgs/msg/Bool"
    });

    var bol = new ROSLIB.Message({
        data: true
    });

    bool_topic.publish(bol);

    // When we receive a message on /twist_topic, add its data as a list item to the “twist_messages" ul
    bool_topic.subscribe((message) => {
        document.getElementById("bool_messages").innerHTML = message.data;
    });
}

function go_home() {
    // Create a listener for /my_topic
    const status_topic = new ROSLIB.Topic({
        ros,
        name: "/status_topic",
        messageType: "std_msgs/String",
    });

    var str = new ROSLIB.Message({
        data: 'Going back Home'
    });

    status_topic.publish(str);

    status_topic.subscribe((message) => {
        document.getElementById("messages").innerHTML = message.data;
    });

    // Create a listener for /twist_topic
    const bool_topic = new ROSLIB.Topic({
        ros,
        name: "/bool_topic",
        messageType: "std_msgs/msg/Bool"
    });

    var bol = new ROSLIB.Message({
        data: false
    });

    bool_topic.publish(bol);

    // When we receive a message on /twist_topic, add its data as a list item to the “twist_messages" ul
    bool_topic.subscribe((message) => {
        document.getElementById("bool_messages").innerHTML = message.data;
    });
}

function emer_stop() {
    // Create a listener for /my_topic
    const status_topic = new ROSLIB.Topic({
        ros,
        name: "/status_topic",
        messageType: "std_msgs/String",
    });

    var str = new ROSLIB.Message({
        data: 'Stopping'
    });

    status_topic.publish(str);

    status_topic.subscribe((message) => {
        document.getElementById("messages").innerHTML = message.data;
    });

    // Create a listener for /twist_topic
    const bool_topic = new ROSLIB.Topic({
        ros,
        name: "/bool_topic",
        messageType: "std_msgs/msg/Bool"
    });

    var bol = new ROSLIB.Message({
        data: false
    });

    bool_topic.publish(bol);

    // When we receive a message on /twist_topic, add its data as a list item to the “twist_messages" ul
    bool_topic.subscribe((message) => {
        document.getElementById("bool_messages").innerHTML = message.data;
    });
}

