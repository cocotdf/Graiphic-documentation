<h1>Particle Analysis</h1>

<h2>Description</h2>

<p>Returns the number of particles detected in a binary image and a 2D array of requested measurements about the particle. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/a0/a0ef2ed5b48b-particle_analysis.png" alt="Particle_Analysis.Png" width="363" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_32.Png" src="/_assets/shared-images/05/052f6e6ea35b-input_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>Pixel Measurements :<em> array, </em></strong>measurement parameters you can request for each particle. The parameters are returned as uncalibrated pixel measurements.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Image_Src.Png" src="/_assets/shared-images/24/24dc58704218-output_image_src.png" width="42"/></td>
      <td valign="top"><strong>Dup Image Src : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_32.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top">Particles Number :<em> integer, </em>indicates the number of particles detected in the image.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Double.Png" src="assets/output_array_double.png" width="42"/></td>
      <td valign="top"><strong>Particle Measurements : <em>array, </em></strong>returns the requested pixel measurements from the detected particles. The array has one column for each measurement. requested in <strong>Pixel Measurements</strong> and one row for each particle detected.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
