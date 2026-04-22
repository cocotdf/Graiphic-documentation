<h1>Write JPEG2000 File</h1>

<h2>Description</h2>

<p>Writes an image to a file in JPEG2000 format. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/44/445400f0b73c-write_jpeg2000_file.png" alt="Write_Jpeg2000_File.Png" width="291" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <i>class, </i></strong>type accepted<strong> U8 </strong>and <strong>RGB</strong><strong>.</strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Path.Png" src="/_assets/shared-images/37/37a46ccf5b9b-path-in.png" width="42"/></td>
      <td valign="top"><strong>File Path : <em>path, </em></strong>file path (JPEG2000).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Boolean.Png" src="/_assets/shared-images/1c/1cd07c2c1382-input_boolean.png" width="42"/></td>
      <td valign="top"><strong>Lossless : <em>boolean, </em></strong>if true do not take into account Compression Rate.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Double.Png" src="/_assets/shared-images/3d/3d70b56b9396-input_double.png" width="42"/></td>
      <td valign="top">Compression Rate : <em>float, </em>file compression rate where 1000 is the highest compression value.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Image_Src.Png" src="/_assets/shared-images/24/24dc58704218-output_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Dst : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Boolean.Png" src="/_assets/shared-images/f4/f4787639135e-output_boolean.png" width="42"/></td>
      <td valign="top"><strong>Succeed? :<em> boolean, </em></strong>true if the operation is successful.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
