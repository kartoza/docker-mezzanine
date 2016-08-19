function FileSubmit(FileURL, MediaFileURL) {
    parentWin = (!window.frameElement && window.dialogArguments) || opener || parent || top;
    parentWin.document.getElementById("id_mugshot").value = FileURL;
    parentWin.document.getElementById("image_id_mugshot").src = MediaFileURL;
    parentWin.document.getElementById("help_id_mugshot").style.display = "inline";
    parentWin.document.getElementById("link_id_mugshot").style.display = "inline";
    parentWin.document.getElementById("clear_id_mugshot").style.display = "inline";
    window.close();
}