<h1>Read Frame</h1>

<h2>Description</h2>

<p>Read the last frame. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/63/63df1e6b0b30-read_frame.png" alt="Read_Frame.Png" width="252" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Session.Png" src="/_assets/shared-images/cb/cbb5c888ebf6-input_session.png" width="42"/></td>
      <td valign="top"><strong>Session Src : <i>class</i></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top">Image Src<i> : class</i></td>
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
    <tr>
      <td width="64" valign="top"><img alt="Output_Image_Src.Png" src="/_assets/shared-images/24/24dc58704218-output_image_src.png" width="42"/></td>
      <td valign="top">Image Dst :<em> class, </em>the type adapts to the image sent by the camera.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Boolean.Png" src="/_assets/shared-images/f4/f4787639135e-output_boolean.png" width="42"/></td>
      <td valign="top">Frame Exist? :<em> boolean, </em>false if the frame doesn’t exist.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>

<h3>Open and play a camera</h3>

<p align="center"><img src="/_assets/shared-images/bb/bbb6ac0d8e68-read_camera.png" alt="read_camera" width="260" /></p>

<p>1 – Initialize</p>

<p>Open camera reference and create a temporary memory location for an image.</p>

<p>2 – Process</p>

<p>Each loop reads the last frame and displays this frame.</p>

<p>3 – Close</p>

<p>We close all open references.</p>
