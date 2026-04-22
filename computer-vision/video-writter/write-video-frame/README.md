<h1>Write Video Frame</h1>

<h2>Description</h2>

<p>Write an image to the video. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/24/24afdae0cbb4-write_video_frame.png" alt="Write_Video_Frame.Png" width="297" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Video_Writer.Png" src="/_assets/shared-images/16/16b3d1ec3851-input_video_writer.png" width="42"/></td>
      <td valign="top"><strong>VideoWriter Src : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong>, <strong>I16</strong>, <strong>RGB</strong> and <strong>HSL</strong>.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Video_Writer.Png" src="/_assets/shared-images/33/33bcb1d285ab-output_video_writer.png" width="42"/></td>
      <td valign="top"><strong>VideoWriter Dst : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Image_Src.Png" src="/_assets/shared-images/24/24dc58704218-output_image_src.png" width="42"/></td>
      <td valign="top"><strong>Dup Image Src : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision library to run it).</p>

<h3>Create and write video</h3>

<p align="center"><img src="/_assets/shared-images/1c/1cd1349db3ce-video_writer_example.png" alt="video_writer_example" width="260" /></p>

<p>1 – Initialize</p>

<p>Open camera reference, create a temporary memory location for an image and create video reference.</p>

<p>2 – Process</p>

<p>Each loop reads the last frame and displays this frame. If the “Record” boolean is true, the image is saved in video.</p>

<p>3 – Close</p>

<p>We close all open references.</p>
