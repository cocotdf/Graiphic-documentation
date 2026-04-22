<h1>Read Image File</h1>

<h2>Description</h2>

<p>Read an image file. The file format can be a standard format (BMP, TIFF, JPEG/JPG, TIFF, GIF, PNG, PPM, PGM and WebP) or a nonstandard format known to the user. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/ca/cafb22033dbb-read_image_file.png" alt="Read_Image_File.Png" width="234" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Path.Png" src="/_assets/shared-images/37/37a46ccf5b9b-path-in.png" width="42"/></td>
      <td valign="top">File Path : <em>path, </em>file path (BMP, TIFF, JPEG/JPG, TIFF, GIF, PNG, PPM, PGM and WebP).</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Image_Src.Png" src="/_assets/shared-images/24/24dc58704218-output_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Dst : <em>class, </em></strong>the type adapts to the image file.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_String.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top">File Type :<em> string, </em>file extension.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Cluster_1.Png" src="/_assets/shared-images/ed/edf449127715-output_cluster_1.png" width="42"/></td>
      <td valign="top"><strong>File Info : <em>cluster,</em> </strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_32.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>Width :<em> integer, </em></strong>image width.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_32.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>Height :<em> integer, </em></strong>image height.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Unsigned_32.Png" src="/_assets/shared-images/7b/7bd02cddb48e-output_unsigned_32.png" width="42"/></td>
      <td valign="top"><strong>Image Type : <em>integer, </em></strong>specifies the type of the image.
<ul>
<li>
<ul>
<li>
<ul>
<li>
<ul>
<li>
<ul>
<li>Grayscale (U8) : 8 bits per pixel (unsigned, standard monochrome)</li>
<li>Grayscale (I16) : 16 bits per pixel (signed)</li>
<li>Grayscale (SGL) : 32 bits per pixel (floating point)</li>
<li>Complex (CSG) : 2 × 32 bits per pixel (floating point)</li>
<li>RGB (U32) : 32 bits per pixel (red, green, blue, alpha)</li>
<li>HSL (U32) : 32 bits per pixel (hue, saturation, luminance, alpha)</li>
<li>RGB (U64) : 64 bits per pixel (red, green, blue, alpha)</li>
<li>Grayscale (U16) : 16 bits per pixel (unsigned)</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img src="/_assets/shared-images/aa/aa516e9c5abd-file_info.png" alt="file_info" width="114" /></p></td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>

<h3>Read an image file</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="50%"><p><a href="https://www.youtube.com/embed/2tLTSuQBt3c?feature=oembed">Get started - Read Image File with TIGR vision toolkit for LabVIEW</a></p></td>
      <td valign="top" width="50%"><p><strong>Code used for this video</strong></p>

<p align="center"><img src="/_assets/shared-images/5d/5d4d5749f72d-read-image.png" alt="Read image" width="260" /></p></td>
    </tr>
  </tbody>
</table>
