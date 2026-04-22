<h1>Get Pixel Line</h1>

<h2>Description</h2>

<p>Extracts the intensity values of a line of pixels. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/71/716b198420e1-get_pixel_line.png" alt="Get_Pixel_Line.Png" width="293" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong> and <strong>I16</strong>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_32.Png" src="/_assets/shared-images/05/052f6e6ea35b-input_array_integer_32.png" width="42"/></td>
      <td valign="top">Line Coordinates : <em>array, </em>array specifying the pixel coordinates that form the end points of the line.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Unsigned_8_.Png" src="/_assets/shared-images/ee/eeb63aea4468-output_array_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>Pixel Line (U8) :<em> array, </em></strong>returns the intensity values for the specified line of pixels. Use this output only when image is an 8-bit image.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_16.Png" src="/_assets/shared-images/7c/7c2ff76ce755-output_array_integer_16.png" width="42"/></td>
      <td valign="top"><strong>Pixel Line (I16) :<em> array, </em></strong>returns the intensity values for the specified line of pixels. Use this output only when image is an 16-bit image​.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
