<h1>Particle Filter</h1>

<h2>Description</h2>

<p>Filters (keeps or removes) each particle in an image according to its measurements. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/a0/a09707caa20e-particle_filter.png" alt="Particle_Filter.Png" width="289" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Boolean.Png" src="/_assets/shared-images/1c/1cd07c2c1382-input_boolean.png" width="42"/></td>
      <td valign="top">Keep/Remove (Keep) :<em> boolean, </em>controls whether particles that meet any of the criteria specified in <strong>Selection Values</strong> are removed. When <strong>Keep/Remove Particles</strong> is TRUE, particles meeting any of the criteria are removed. If FALSE, only particles meeting any of the criteria remain.</td>
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
      <td valign="top"><strong>Selection Values :<em> array, </em></strong>controls the criteria used to filter the particle in the image.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Double.Png" src="/_assets/shared-images/3d/3d70b56b9396-input_double.png" width="42"/></td>
      <td valign="top"><strong>Min : <em>float, </em></strong>specifies the lower value of the range for the chosen parameter.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Double.Png" src="/_assets/shared-images/3d/3d70b56b9396-input_double.png" width="42"/></td>
      <td valign="top"><strong> Max : <em>float, </em></strong>specifies the upper value of the range for the chosen parameter.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Enum.Png" src="/_assets/shared-images/5c/5c2b52d3b208-input_enum.png" width="42"/></td>
      <td valign="top"><strong> Measurement Parameter : <em>enum, </em></strong>is the measurement on which you want to filter.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Boolean.Png" src="/_assets/shared-images/1c/1cd07c2c1382-input_boolean.png" width="42"/></td>
      <td valign="top"><strong> In/Out (In) : <em>boolean, </em></strong>specifies whether to include or exclude the values given in <strong>Min</strong> and <strong>Max</strong>.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table>

<p>When In/Out is false, the particle meets the criteria if <strong>Min</strong> ≤ particle measurement &lt; <strong>Max</strong>.<br/>When In/Out is true, the particle meets the criteria if <strong>Max</strong> ≤ particle measurement  &lt; <strong>Min</strong>.</p></td>
      <td valign="top" width="30%"><p align="center"><img src="assets/selection_values.png" alt="selection_values" width="260" /></p></td>
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
