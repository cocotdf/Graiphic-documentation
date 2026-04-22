<h1>Open Video</h1>

<h2>Description</h2>

<p>Create video session reference from the path file. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/74/74aab104898a-open_video.png" alt="Open_Video.Png" width="232" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Path.Png" src="/_assets/shared-images/37/37a46ccf5b9b-path-in.png" width="42"/></td>
      <td valign="top"><strong>File Path : <em>path, </em></strong>path of the video.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Session.Png" src="/_assets/shared-images/86/8603666de7ad-output_session.png" width="42"/></td>
      <td valign="top"><strong>Session Dst : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Cluster_2.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="42"/></td>
      <td valign="top"><strong>Frame Data : <em>cluster, </em></strong>cluster containing information about the video.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Unsigned_32.Png" src="/_assets/shared-images/7b/7bd02cddb48e-output_unsigned_32.png" width="42"/></td>
      <td valign="top"><strong>Width : <em>integer, </em></strong>specifies the width of the image.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Unsigned_32.Png" src="/_assets/shared-images/7b/7bd02cddb48e-output_unsigned_32.png" width="42"/></td>
      <td valign="top">Height : <em>integer,</em> specifies the height of the image.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_32.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>Image Type :<em> integer, </em></strong>specifies the type of image used in the video file.
<ul>
<li>
<ul>
<li>
<ul>
<li>Grayscale (U8) : 8 bits per pixel (unsigned, standard monochrome)</li>
<li>RGB (U32) : 32 bits per pixel (red, green, blue, alpha)</li>
<li>HSL (U32) : 32 bits per pixel (hue, saturation, luminance, alpha)</li>
</ul>
</li>
</ul>
</li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_32.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top">Num Frames : <em>integer, </em>number of frames.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Unsigned_32.Png" src="/_assets/shared-images/7b/7bd02cddb48e-output_unsigned_32.png" width="42"/></td>
      <td valign="top">Frames Per Second : <em>integer, </em>specifies the frame per second of the video.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_64.Png" src="/_assets/shared-images/97/975b537e9c31-output_interger_64.png" width="42"/></td>
      <td valign="top"><strong>Loop timing : <em>integer, </em></strong>period between two images.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_String.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top">Codec :<em> string, </em>specifies the codec used to create the video file.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Boolean.Png" src="/_assets/shared-images/f4/f4787639135e-output_boolean.png" width="42"/></td>
      <td valign="top">Has Data :<em> boolean, </em>false if video file is empty.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img src="/_assets/shared-images/1f/1f6c9f2f5f27-frame_data.png" alt="frame_data" width="107" /></p></td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>

<h3>Open and play a video</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="50%"><p><a href="https://www.youtube.com/embed/P9mON_WxFQg?feature=oembed">Get started - Play a Video File with TIGR vision toolkit for LabVIEW</a></p></td>
      <td valign="top" width="50%"><p><strong>Code used for this video</strong></p>

<p align="center"><img src="/_assets/shared-images/71/71c88ab40862-play_video.png" alt="play_video" width="260" /></p></td>
    </tr>
  </tbody>
</table>
