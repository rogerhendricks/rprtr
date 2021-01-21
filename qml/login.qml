import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window
    width: 400
    height: 500
    visible: true
    title: qsTr("Login Page")


    flags: Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.Dialog | Qt.WindowTitleHint


    // Set Material Style
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    QtObject {
        id: internal
        property string user: "admin"
        property string pass: "admin"

        function checkLogin(username, password) {
            if(username === user && password === pass){
                var component = Qt.createComponent("main.qml")
                var win = component.createObject()
                win.show()
                visible = false
            } else {
                if(username !== user){
                    usernameField.Material.foreground = Material.Pink
                    usernameField.Material.accent = Material.Pink
                } else {
                    usernameField.Material.foreground = Material.LightBlue
                    usernameField.Material.accent = Material.LightBlue
                }


                if(password !== pass ){
                    passwordField.Material.foreground = Material.Pink
                    passwordField.Material.accent = Material.Pink
                } else {
                    passwordField.Material.foreground = Material.LightBlue
                    passwordField.Material.accent = Material.LightBlue
                }

            }
        }
    }

    // Top Bar
    Rectangle{
        id: topBar
        height: 40
        color: Material.color(Material.Blue)
        anchors{
            left: parent.left
            right: parent.right
            top: parent.top
            margins: 10
        }
        radius: 10
        Text{
            text: qsTr("LOGIN PAGE")
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignCenter
            verticalAlignment: Text.AlignCenter
            color: "#ffffff"
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 10
        }
    }
    TextField{
        id: usernameField
        width: 300
        text: qsTr("")
        selectByMouse: true
        placeholderText: qsTr("Your Username or Email")
        verticalAlignment: Text.AlignCenter
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: topBar.bottom
        anchors.topMargin: 60
    }
    TextField{
    id: passwordField
    width: 300
    text: qsTr("")
    selectByMouse: true
    placeholderText: qsTr("Your Password")
    verticalAlignment: Text.AlignCenter
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.top: usernameField.bottom
    anchors.topMargin: 10
    echoMode: TextInput.Password
    }
    Button{
        id: buttonLogin
        width: 300
        text: qsTr("Login")
        anchors.top: passwordField.bottom
        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: internal.checkLogin(usernameField.text, passwordField.text)
    }

}