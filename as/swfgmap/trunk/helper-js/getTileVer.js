function getGoogleMapsTileVersion()
{
	if (!GLoad.toString().match(/mt[0-3][^"]*/))
		return null;

	var tileurl = RegExp["$&"];
	if (!tileurl.match(/v=([^&]+)/))
		return null;

	return RegExp["$1"];
}
