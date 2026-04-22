<h1>Segmentation Masks</h1>

<h2>Description</h2>

<p>The Segmentation Mask function merges a base image with multiple color masks using a given opacity factor for every mask, producing a partially masked image. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/c3/c34a032574c7-segmentation_masks.png" alt="Segmentation_Masks.Png" width="247" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>RGB</strong> and <strong>HSL</strong>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Image_Src.Png" src="/_assets/shared-images/29/2950193b48f6-input_array_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Masks : <em>array, </em></strong>type accepted <strong>RGB</strong> and <strong>HSL</strong>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Single.Png" src="/_assets/shared-images/00/0011264bc6a4-input_array_single.png" width="42"/></td>
      <td valign="top">Coefficients : <em>float, </em>parameter defining the transparency of masks on the original image. From 0 = opaque to 1 = transparent.</td>
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
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
