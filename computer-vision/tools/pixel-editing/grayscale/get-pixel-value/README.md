<h1>Get Pixel Value</h1>

<h2>Description</h2>

<p>Reads a pixel value from an image. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/c7/c751418a727d-get_pixel_value.png" alt="Get_Pixel_Value.Png" width="267" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong> and <strong>I16</strong>.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Cluster_1.Png" src="/_assets/shared-images/d3/d3e052622960-input_cluster_1.png" width="42"/></td>
      <td valign="top"><strong>Coordinate : <em>cluster,</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_32.Png" src="/_assets/shared-images/61/616a739c55d0-input_interger_32.png" width="42"/></td>
      <td valign="top"><strong>X :<em> integer, </em></strong>horizontal coordinate of the pixel.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_32.Png" src="/_assets/shared-images/61/616a739c55d0-input_interger_32.png" width="42"/></td>
      <td valign="top">Y :<em> integer, </em>vertical coordinate of the pixel.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img src="/_assets/shared-images/e8/e82bccc71c1a-coordinate.png" alt="coordinate" width="79" /></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Unsigned_8.Png" src="/_assets/shared-images/99/99f7538c1dee-output_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>Pixel Value (U8) : <em>integer, </em></strong>returns the specified pixel value. This output is used only for an 8-bit image.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_16.Png" src="/_assets/shared-images/c0/c0ce9ef8706b-output_interger_16.png" width="42"/></td>
      <td valign="top"><strong>Pixel Value (I16) : <em>integer, </em></strong>returns the specified pixel value. This output is used only for an 16-bit image.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
