import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window
    width: 640
    height: 480
    visible: true
    title: qsTr("Main Page")

    flags: Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.Dialog | Qt.WindowTitleHint


    // Set Material Style
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

}