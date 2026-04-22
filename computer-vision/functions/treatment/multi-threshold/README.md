<h1>Multi Threshold</h1>

<h2>Description</h2>

<p>Performs thresholds of multiple intensity ranges to an image. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/34/346708ec0ec0-multi_threshold.png" alt="Multi_Threshold.Png" width="234" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong>, <strong>I16</strong>, <strong>RGB</strong> and <strong>HSL.</strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Cluster_2.Png" src="/_assets/shared-images/7c/7c2884d81fe7-cluster-array-in.png" width="42"/></td>
      <td valign="top"><strong>Ranges :<em> array,</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_32.Png" src="/_assets/shared-images/61/616a739c55d0-input_interger_32.png" width="42"/></td>
      <td valign="top"><strong>Lower Threshold : <em>integer, </em></strong>is the lowest pixel value to be taken into account during a threshold.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_32.Png" src="/_assets/shared-images/61/616a739c55d0-input_interger_32.png" width="42"/></td>
      <td valign="top">Higher Threshold :<em> integer, </em>is the highest pixel value to be taken into account during a threshold.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_32.Png" src="/_assets/shared-images/61/616a739c55d0-input_interger_32.png" width="42"/></td>
      <td valign="top">Replace Value :<em> integer, </em>is the value used to replace pixels between the <strong>Lower value</strong> and <strong>Higher value</strong>. This operation requires that <strong>Keep/Replace Value</strong> is TRUE.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Boolean.Png" src="/_assets/shared-images/1c/1cd07c2c1382-input_boolean.png" width="42"/></td>
      <td valign="top">Keep/Replace Value :<em> boolean, </em>determines whether to replace the value of the pixels existing in the range between <strong>Lower value</strong> and <strong>Higher value</strong>. The default status, TRUE, replaces these pixel values, and the status FALSE keeps the original values.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table>

<p>All pixels outside the range between<strong> Lower value</strong> and <strong>Higher value</strong> are set to 0. All values found between this range are replaced by the value entered in <strong>Replace Value</strong> if <strong>Keep/Replace Value</strong> is TRUE.</p></td>
      <td valign="top" width="30%"><p align="center"><img src="assets/ranges.png" alt="ranges" width="218" /></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Image_Src.Png" src="/_assets/shared-images/24/24dc58704218-output_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Dst :<em> class</em></strong></td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
