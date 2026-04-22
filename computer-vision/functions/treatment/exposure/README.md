<h1>Exposure</h1>

<h2>Description</h2>

<p>Converts Src pixel values to the Dst image according to this formula ((a(*Src)(x,y)+ß)).​ Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/db/db6cb845e421-exposure.png" alt="Exposure.Png" width="234" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong>, <strong>I16</strong>, <strong>RGB</strong> and <strong>HSL.</strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Single.Png" src="/_assets/shared-images/fd/fd47ddc3550b-input_single.png" width="42"/></td>
      <td valign="top">alpha : <em>float</em>, optional scale factor.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_32.Png" src="/_assets/shared-images/61/616a739c55d0-input_interger_32.png" width="42"/></td>
      <td valign="top"><strong>beta : <em>integer</em>, </strong>optional delta added to the scaled values.</td>
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
