var notificationInterval;

function startNotificationInterval() {
    checkAndShowNotification();

    // Set the interval to check every hour (adjust as needed)
    notificationInterval = setInterval(function() {
        var currentTime = new Date().getTime();
        var lastNotificationTime = localStorage.getItem('lastNotificationTime');

        if (!lastNotificationTime || currentTime - lastNotificationTime >= 24 * 60 * 60 * 1000) { // 24 hours
            showNotification();
            localStorage.setItem('lastNotificationTime', currentTime);
        }
    }, 60 * 60 * 1000); // Check every hour
}

function checkAndShowNotification() {
    var lastNotificationTime = localStorage.getItem('lastNotificationTime');
    var currentTime = new Date().getTime();
    var oneDay = 24 * 60 * 60 * 1000; // 24 hours in milliseconds

    if (!lastNotificationTime || currentTime - lastNotificationTime >= oneDay) {
        showNotification();
        localStorage.setItem('lastNotificationTime', currentTime);
    }
}

function showNotification() {
    var notificationContainer = document.getElementById("notificationContainer");
    notificationContainer.style.display = "block";

    setTimeout(function() {
        notificationContainer.style.display = "none";
    }, 3000);
}

function closeNotification() {
    var notificationContainer = document.getElementById("notificationContainer");
    notificationContainer.style.display = "none";
}

function toggleNotifications() {
    var isChecked = document.getElementById("notification-switch").checked;
    if (isChecked) {
        localStorage.setItem("notificationsEnabled", "true");
        startNotificationInterval();
    } else {
        localStorage.setItem("notificationsEnabled", "false");
        clearInterval(notificationInterval);
    }
}

window.onload = function() {
    const toggleButton = document.getElementById("notification-switch");
    if (toggleButton) {
        if (localStorage.getItem("notificationsEnabled") === "true") {
            toggleButton.checked = true;
            startNotificationInterval();
        }
    }
};
